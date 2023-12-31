/**************************

Original script, code and source by

http://www.dynamicdrive.com/dynamicindex4/fullscreenimageviewer/
http://www.dynamicdrive.com/dynamicindex4/zoomio/index.htm

You can read here too

https://beben-koben.blogspot.com/2017/07/jquery-full-screen-image-viewer-zoom.html

**************************/

!(function (i) {
  function e(i) {
    var e = Math.min(
      window.innerWidth / i.width,
      window.innerHeight / i.height
    );
    return e;
  }
  function t(t, n) {
    a ||
      (i(document.body).append(r),
      (a = i("#fullscreencanvas")),
      (s = i("#fullscreenimagearea")),
      (d = i("#closeviewer")),
      (l = i("#fullimageloadingdiv")),
      d.on("click", function () {
        i(document.body).removeClass("revealviewer"),
          s.data("$largeimage").unbind(),
          s.empty(),
          l.css("visibility", "hidden");
      }));
    var o = t.attr("data-scale") || n.scale,
      c = t.attr("data-large") || n.largeimage || t.attr("src");
    t.on("click", function () {
      i(document.body).addClass("revealviewer"),
        this.getAttribute("data-large") && l.css("visibility", "visible");
      var t = new Image(),
        n = i(t);
      n.on("load", function () {
        var i = e(t);
        if (
          (s.html(
            '<img src="' +
              t.src +
              '" style="width:' +
              t.width * i +
              "px; height:" +
              t.height * i +
              'px;" />'
          ),
          l.css("visibility", "hidden"),
          o > 1)
        ) {
          var n = s.find("img:eq(0)");
          n.zoomio({ scale: o, fixedcontainer: !0 });
        }
      }),
        (t.src = c),
        s.data("$largeimage", n);
    });
  }
  var n = window.matchMedia
      ? window.matchMedia("screen and (max-device-width: 680px)")
      : { matches: !1, addListener: function () {} },
    o = { scale: 1 },
    a = null,
    s = null,
    d = null,
    l = null,
    r =
      '<div id="fullscreencanvas"><div id="fullscreenimagearea"></div></div><div id="fullimageloadingdiv"><div class="spinner"></div></div><div id="closeviewer" title="Close Viewer">Close</div>';
  i.fn.fullscreenimage = function (e) {
    var a = i.extend({}, o, e);
    return this.each(function () {
      var e = i(this);
      return (
        (e = e.is("img") ? e : e.find("img:eq(0)")),
        0 == e.length || n.matches ? !0 : void t(e, a)
      );
    });
  };
})(jQuery);

!(function (i) {
  function t(i) {
    return { w: i.width(), h: i.height() };
  }
  function e(i, t) {
    return i.offsetParent ? i[t] + e(i.offsetParent, t) : i[t];
  }
  function o(o, c) {
    var r = c || a,
      u = l ? "click" : "mouseenter";
    o.off(u).on(u, function (a) {
      if (
        "visible" != n.css("visibility") ||
        1 != n.queue("fx").length ||
        f != o
      ) {
        f = o;
        var u,
          h = a,
          a = h.originalEvent.changedTouches
            ? h.originalEvent.changedTouches[0]
            : h;
        if (1 == c.fixedcontainer) {
          var v = o.offset();
          u = { left: v.left, top: v.top };
        } else
          u = {
            left: e(o.get(0), "offsetLeft"),
            top: e(o.get(0), "offsetTop"),
          };
        var p = [a.pageX - u.left, a.pageY - u.top],
          m = t(o),
          g = r.w || m.w,
          b = r.h || m.h;
        n.stop().css({ visibility: "hidden" });
        var y,
          w = i.Deferred(),
          z = o.attr("data-largesrc") || o.data("largesrc") || o.attr("src");
        o.data("largesrc") &&
          s.css({
            width: m.w,
            height: m.h,
            left: u.left,
            top: u.top,
            visibility: "visible",
            zIndex: 1e4,
          }),
          n.html('<img src="' + z + '">'),
          (y = n.find("img")),
          y.get(0).complete
            ? w.resolve()
            : y.on("load", function () {
                w.resolve();
              }),
          w.done(function () {
            n.css({ width: g, height: b, left: u.left, top: u.top });
            var i = t(n);
            c.scale && y.css({ width: o.width() * c.scale });
            var e = t(y);
            if (
              (s.css({ zIndex: 9998 }),
              n
                .stop()
                .css({ visibility: "visible", opacity: 0 })
                .animate({ opacity: 1 }, r.fadeduration, function () {
                  s.css({ visibility: "hidden" });
                }),
              l)
            ) {
              var a = (p[0] / m.w) * (e.w - i.w),
                f = (p[1] / m.h) * (e.h - i.h);
              n.scrollLeft(a), n.scrollTop(f);
            }
            d = {
              $zoomimage: y,
              offset: u,
              settings: r,
              multiplier: [e.w / i.w, e.h / i.h],
            };
          }),
          o.off("mouseleave").on("mouseleave", function () {
            "resolved" != w.state() &&
              (w.reject(), s.css({ visibility: "hidden" }));
          }),
          h.stopPropagation();
      }
    });
  }
  var n,
    s,
    a = { fadeduration: 500 },
    d = { $zoomimage: null, offset: [,], settings: null, multiplier: [,] },
    f = i(),
    l =
      null !=
      navigator.userAgent.match(/(iPad)|(iPhone)|(iPod)|(android)|(webOS)/i);
  (i.fn.zoomio = function (t) {
    var e = i.extend({}, a, t);
    return this.each(function () {
      var t = i(this);
      return (
        (t = t.is("img") ? t : t.find("img:eq(0)")),
        0 == t.length ? !0 : void o(t, e)
      );
    });
  }),
    i(function () {
      (n = i('<div id="zoomiocontainer">').appendTo(document.body)),
        (s = i(
          '<div id="zoomioloadingdiv"><div class="spinner"></div></div>'
        ).appendTo(document.body)),
        l
          ? (n.addClass("mobileclass"),
            n.on("touchstart", function (i) {
              i.stopPropagation();
            }),
            i(document).on("touchstart.dismisszoomio", function () {
              d.$zoomimage &&
                (s.css({ visibility: "hidden" }),
                n
                  .stop()
                  .animate(
                    { opacity: 0 },
                    d.settings.fadeduration,
                    function () {
                      i(this).css({
                        visibility: "hidden",
                        left: "-100%",
                        top: "-100%",
                      });
                    }
                  ));
            }))
          : (n.on("mouseenter", function () {}),
            n.on("mousemove", function (i) {
              var t = d.$zoomimage,
                e = d.offset,
                o = [i.pageX - e.left, i.pageY - e.top],
                n = d.multiplier;
              t.css({ left: -o[0] * n[0] + o[0], top: -o[1] * n[1] + o[1] });
            }),
            n.on("mouseleave", function () {
              s.css({ visibility: "hidden" }),
                n
                  .stop()
                  .animate(
                    { opacity: 0 },
                    d.settings.fadeduration,
                    function () {
                      i(this).css({
                        visibility: "hidden",
                        left: "-100%",
                        top: "-100%",
                      });
                    }
                  );
            }));
    });
})(jQuery);

jQuery(function () {
  $("img.thumbnails").fullscreenimage({
    scale: 2,
  });
  $(".zoomio").zoomio({
    fadeduration: 500,
  });
  $(".nolargeimg").zoomio({
    w: "500px",
    h: "400px",
  });
});
